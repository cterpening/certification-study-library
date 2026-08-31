(() => {
  const searchDialog = document.querySelector('.md-search[role="dialog"]');
  if (searchDialog && !searchDialog.hasAttribute("aria-label")) {
    searchDialog.setAttribute("aria-label", "Site search");
  }

  document
    .querySelectorAll('.task-list-item input[type="checkbox"]')
    .forEach((checkbox, index) => {
      if (checkbox.hasAttribute("aria-label")) return;
      const itemText = checkbox.closest("li")?.textContent?.trim();
      checkbox.setAttribute(
        "aria-label",
        itemText || `Readiness checklist item ${index + 1}`,
      );
    });
})();
