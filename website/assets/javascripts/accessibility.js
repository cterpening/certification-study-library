(() => {
  const searchDialog = document.querySelector('.md-search[role="dialog"]');
  if (searchDialog && !searchDialog.hasAttribute("aria-label")) {
    searchDialog.setAttribute("aria-label", "Site search");
  }
})();
