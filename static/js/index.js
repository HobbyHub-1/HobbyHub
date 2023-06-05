// card 게시물 상단 좋아요 비동기(하트 아이콘)
let likeforms = document.querySelectorAll( `.like-form` );
const csrftoken = document.querySelector( `[name=csrfmiddlewaretoken]` ).value;

likeforms.forEach((form) => {
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    const postId = event.target.dataset.postId;
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/posts/${postId}/post_likes/`,
      headers: {
        'X-CSRFToken': csrftoken
      }
    })
    .then((response) => {
      const isLiked = response.data.is_liked;
      const heartIcon = form.querySelector( `#post-heart`);
        if (isLiked === true) {
            heartIcon.classList.remove('bi-heart');
            heartIcon.classList.add('bi-heart-fill');
          } else {
            heartIcon.classList.remove('bi-heart-fill');
            heartIcon.classList.add('bi-heart');
        }
      })
    .catch((error) => {
      console.log(error.response);
    });
  });
});


// 태그 버튼 클릭 이벤트 처리
const tagButtons = document.querySelectorAll('.hobby-tags-btn');
tagButtons.forEach(button => {
  button.addEventListener('click', () => {
    const selectedTag = button.dataset.slug;
    filterPostsByTag(selectedTag);
  });
});
// 게시물 필터링 함수
function filterPostsByTag(tag) {
  const posts = document.querySelectorAll('.card_single');
  posts.forEach(post => {
    const postTags = post.dataset.tags.split(',');
    if (postTags.includes(tag) || tag === 'all') {
      post.style.display = 'inline'; // 선택된 태그와 일치하는 게시물은 보이도록 설정
    } else {
      post.style.display = 'none'; // 선택된 태그와 일치하지 않는 게시물은 숨김 처리
    }
  });
}
// 페이지 로드시 초기 필터링 설정
document.addEventListener('DOMContentLoaded', () => {
  const initialTag = document.querySelector('.hobby-tags-btn-active').dataset.slug;
  filterPostsByTag(initialTag);
});
