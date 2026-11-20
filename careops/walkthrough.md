# Walkthrough | Review an administrative onboarding checklist

**Format:** A read-through of the decision flow using the fictional onboarding SOP. The examples below describe expected behavior. The evidence table in the [case study](README.md) identifies which paths were exercised.

1. **Request a checklist.** A coordinator asks for onboarding tasks. The agent selects `ONBOARDING-001`, version 1.1, and previews three proposed tasks.
2. **Reject the preview.** Consider a coordinator who spots a mismatch. Rejection ends the proposal without creating tasks. Showing a preview has no effect on the saved task list.
3. **Approve a fresh preview.** Once the proposed tasks match the SOP, approval allows the system to save the canonical tasks and return them to the reviewer.
4. **Repeat the approval.** A second submission of the same approval should return the existing tasks. The retained acceptance record covers this bounded case.

**Discussion prompt:** A browser loses the response just after the first approval. Which facts should the server preserve so a retry can recover the result? A live session can be shown by the project owner through the authenticated interface.
