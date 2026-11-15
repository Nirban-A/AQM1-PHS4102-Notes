/* Box titles of the form "Title || Source" show the source as a tag in the
   top-right corner of the box (e.g. "Griffiths, Example 9.3"). */
function moveSourceTags() {
  document.querySelectorAll(".admonition-title, summary").forEach(function (el) {
    if (el.querySelector(".src-tag")) return;
    var nodes = Array.prototype.slice.call(el.childNodes);
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];
      if (n.nodeType !== 3 || n.nodeValue.indexOf("||") === -1) continue;
      var parts = n.nodeValue.split("||");
      var span = document.createElement("span");
      span.className = "src-tag";
      span.appendChild(document.createTextNode(parts.slice(1).join("||").trim()));
      for (var j = i + 1; j < nodes.length; j++) span.appendChild(nodes[j]);
      n.nodeValue = parts[0].replace(/\s+$/, "");
      el.appendChild(span);
      break;
    }
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(moveSourceTags);
} else {
  document.addEventListener("DOMContentLoaded", moveSourceTags);
}
