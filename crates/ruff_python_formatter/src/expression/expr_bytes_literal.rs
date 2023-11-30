use ruff_python_ast::AnyNodeRef;
use ruff_python_ast::ExprBytesLiteral;

use crate::comments::SourceComment;
use crate::expression::expr_string_literal::is_multiline_string;
use crate::expression::parentheses::{NeedsParentheses, OptionalParentheses};
use crate::expression::string::{AnyString, FormatString};
use crate::prelude::*;
use crate::preview::is_prefer_splitting_right_hand_side_of_assignments_enabled;
use crate::statement::stmt_assign::is_assignment_with_splittable_targets;

#[derive(Default)]
pub struct FormatExprBytesLiteral;

impl FormatNodeRule<ExprBytesLiteral> for FormatExprBytesLiteral {
    fn fmt_fields(&self, item: &ExprBytesLiteral, f: &mut PyFormatter) -> FormatResult<()> {
        FormatString::new(&AnyString::Bytes(item)).fmt(f)
    }

    fn fmt_dangling_comments(
        &self,
        _dangling_comments: &[SourceComment],
        _f: &mut PyFormatter,
    ) -> FormatResult<()> {
        // Handled as part of `fmt_fields`
        Ok(())
    }
}

impl NeedsParentheses for ExprBytesLiteral {
    fn needs_parentheses(
        &self,
        parent: AnyNodeRef,
        context: &PyFormatContext,
    ) -> OptionalParentheses {
        if self.value.is_implicit_concatenated() {
            OptionalParentheses::Multiline
        } else if is_multiline_string(self.into(), context.source()) {
            OptionalParentheses::Never
        } else if is_prefer_splitting_right_hand_side_of_assignments_enabled(context)
            && is_assignment_with_splittable_targets(parent, context)
        {
            OptionalParentheses::Multiline
        } else {
            OptionalParentheses::BestFit
        }
    }
}
