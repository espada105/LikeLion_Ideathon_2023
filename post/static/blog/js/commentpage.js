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
      // 저장 로직을 추가해야댐
      alert("저장되었습니다.");
    }
  }
  
  "use strict"

const commentInput = document.getElementsByClassName('post')[0];
const submit = document.getElementsByClassName('submit')[0];

/* ---------------------------------------- */
/* 버튼 활성화 */
/* ---------------------------------------- */

commentInput.addEventListener('keyup',submitBtn);

function submitBtn(){
    commentInput.value.length !== 0 ? 
    submit.disabled = false : submit.disabled = true;
}

/* ---------------------------------------- */
/* 댓글 생성 */
/* ---------------------------------------- */

function enterComment() {
    const [comments] = document.getElementsByClassName('comments');
    const newComment = document.createElement('li');
    const comment = `
    <b>dltjsgho</b> 
    ${commentInput.value} 
    <span class="commentLikes"></span>
    <span class="deleted">x</span>
    `; 

    newComment.innerHTML = comment
    comments.appendChild(newComment);
    commentInput.value= '';

/* ---------------------------------------- */
/* heart생성 */
/* ---------------------------------------- */
    const overSizeHeart = newComment.querySelector('.commentLikes');
    const heartIcon = document.createElement("img");

    overSizeHeart.appendChild(heartIcon)
    heartIcon.setAttribute("src", "../img/heart.png");
    
/* ---------------------------------------- */
/* 댓글 삭제 */
/* ---------------------------------------- */
    const deleteTxt = newComment.querySelector('.deleted');

    deleteTxt.addEventListener('click', () => {
        newComment.remove();
    })
}

commentInput.addEventListener('keyup',function(e){
    if(e.code === 'Enter' && commentInput.value.length > 0) {
        enterComment();
    }
    submitBtn();
})

submit.addEventListener('click',()=>{
    if(commentInput.value.length > 0) {
        enterComment();
    }
    submitBtn()
})

function changeImage() {
  var image = document.getElementById("myImage");
  image.src = "새로운이미지.jpg";
}

var count = 0; // 초기 좋아요 수
    function like() {
      count++;
      document.getElementById("count").innerHTML = count;
    }