// 더보기 버튼 기능
let visibleCount = 8; // 초기에 보여지는 게시물 수
const incrementCount = 12; // 더보기 버튼을 클릭할 때마다 추가로 보여지는 게시물 수
const morePostsDivs = document.querySelectorAll('.morePosts');
const newPostsBtn = document.getElementById('newPostsBtn');

// 초기에 일부 게시물 숨기기
for (let i = visibleCount; i < morePostsDivs.length; i++) {
  morePostsDivs[i].hidden = true;
}

newPostsBtn.addEventListener('click', () => {
  for (let i = visibleCount; i < visibleCount + incrementCount; i++) {
    if (morePostsDivs[i]) {
      morePostsDivs[i].hidden = false;
    } else {
      newPostsBtn.style.display = 'none';
      break;
    }
  }
  visibleCount += incrementCount;
});

// 태그 버튼 클릭 이벤트 처리
var tagButtons = document.querySelectorAll('.hobby-tags-btn');
tagButtons.forEach(button => {
  button.addEventListener('click', () => {
    const selectedTag = button.dataset.slug;
    filterPostsByTag(selectedTag);
  });
});

// 게시물 필터링 함수
function filterPostsByTag(tag) {
  const posts = document.querySelectorAll('.tag-button');
  posts.forEach(post => {
    const postTags = post.dataset.tags.split(',');
    console.log(postTags)
    console.log(post.data)
    if (postTags.includes(tag) || tag === 'all') {
      post.style.display = 'inline'; // 선택된 태그와 일치하는 게시물은 보이도록 설정
    } else {
      post.style.display = 'none'; // 선택된 태그와 일치하지 않는 게시물은 숨김 처리
    }
  });
}

// 페이지 로드시 초기 필터링 설정
// window.addEventListener('DOMContentLoaded', () => {
//   const initialTag = document.querySelector('.hobby-tags-btn-active').dataset.slug;
//   filterPostsByTag(initialTag);
// });