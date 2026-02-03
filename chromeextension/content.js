function getEmailText() {
  let email = document.querySelector(".a3s");
  return email ? email.innerText : "No email content found.";
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getEmail") {
    sendResponse({ text: getEmailText() });
  }
});
