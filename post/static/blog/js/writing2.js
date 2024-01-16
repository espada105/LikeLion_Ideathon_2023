document.addEventListener("DOMContentLoaded", function () {
  var shareButton = document.querySelector(".shareButton");
  var dropdown = document.querySelector(".dropdown");

  shareButton.addEventListener("click", function () {
    dropdown.style.display =
      dropdown.style.display === "none" ? "block" : "none";
  });

  // Close the dropdown when clicking outside of it
  document.addEventListener("click", function (event) {
    if (
      !shareButton.contains(event.target) &&
      !dropdown.contains(event.target)
    ) {
      dropdown.style.display = "none";
    }
  });
});


function showConfirmation() {
  var result = confirm("저장하시겠습니까?");
  if (result) {
    // 저장 로직을 추가하세요
    alert("저장되었습니다.");
  }
}
