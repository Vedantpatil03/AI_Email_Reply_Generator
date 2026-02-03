document.getElementById("generate").addEventListener("click", async () => {
  let tone = document.getElementById("tone").value;

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(
      tabs[0].id,
      { action: "getEmail" },
      async (response) => {
        let emailText = response.text;

        let res = await fetch("http://localhost:8000/generate-reply", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ emailText: emailText, tone: tone })
        });

        let data = await res.json();
        document.getElementById("replyBox").value = data.reply;
      }
    );
  });
});

document.getElementById("insert").addEventListener("click", () => {
  let reply = document.getElementById("replyBox").value;

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      function: insertReply,
      args: [reply]
    });
  });
});

function insertReply(text) {
  let box = document.querySelector('[role="textbox"]');
  if (box) {
    box.innerText = text;
  }
}
