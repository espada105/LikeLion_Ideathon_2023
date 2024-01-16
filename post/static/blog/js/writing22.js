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


function openNewWindow() {
  window.open("", "_blank", "width=400,height=400");
}

$(function(){ 

  $("a").click(function(){
    $(".modal").fadeIn();
  });
  
  $(document).keydown(function(event) {
    if (event.which === 27) { 
      $(".modal").fadeOut();
    }
  });
});

const overSizeHeart = newComment.querySelector('.commentLikes');
    const heartIcon = document.createElement("img");

    overSizeHeart.appendChild(heartIcon)
    heartIcon.setAttribute("src", "../img/heart.png");
    
var count = 0; // 초기 좋아요 수
    function like() {
      count++;
      document.getElementById("count").innerHTML = count;
    }