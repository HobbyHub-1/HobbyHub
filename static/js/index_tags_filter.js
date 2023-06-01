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
  const posts = document.querySelectorAll('.post');
  
  posts.forEach(post => {
    const postTags = post.dataset.tags.split(',');
    if (postTags.includes(tag) || tag === 'all') {
      post.style.display = 'block'; // 선택된 태그와 일치하는 게시물은 보이도록 설정
    } else {
      post.style.display = 'none'; // 선택된 태그와 일치하지 않는 게시물은 숨김 처리
    }
  });
}
