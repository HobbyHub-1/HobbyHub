function copyToClipboard(text) {
  const textarea = document.createElement('textarea');
  textarea.value = text;
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand('copy');
  document.body.removeChild(textarea);
  
  const notification = document.createElement('div');
  notification.innerText = '이메일 주소가 복사되었습니다.';
  notification.style.position = 'fixed';
  notification.style.bottom = '10px';
  notification.style.left = '50%';
  notification.style.transform = 'translateX(-50%)';
  notification.style.background = '#f2f2f2';
  notification.style.padding = '10px';
  notification.style.borderRadius = '5px';
  notification.style.boxShadow = '0 2px 5px rgba(0, 0, 0, 0.2)';
  
  document.body.appendChild(notification);
  setTimeout(function() {
    document.body.removeChild(notification);
  }, 3000);
}


document.addEventListener('DOMContentLoaded', function() {
  const followForms = document.getElementsByClassName('follow-form');

  Array.from(followForms).forEach(function(form) {
    form.addEventListener('submit', function(event) {
      event.preventDefault(); // 폼 제출 기본 동작 방지

      const csrfToken = form.getElementsByTagName('input')[0].value; // CSRF 토큰 값 가져오기
      const isFollowed = form.getElementsByClassName('btn')[0].value === '언팔로우'; // 현재 팔로우 상태
      const userPk = form.getAttribute('data-user-id'); // 사용자 고유 식별자

      const xhr = new XMLHttpRequest();
      xhr.open('POST', '/accounts/' + userPk + '/follow/');
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      xhr.setRequestHeader('X-CSRFToken', csrfToken);

      xhr.onload = function() {
        if (xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);

          const followButton = form.getElementsByClassName('btn')[0];
          const followerCount = document.getElementById('follower-count');

          if (isFollowed) {
            followButton.value = '팔로우';
            followButton.classList.remove('btn-dark');
            followButton.classList.add('btn-outline-dark');
            followerCount.textContent = response.follower_count;
          } else {
            followButton.value = '언팔로우';
            followButton.classList.remove('btn-outline-dark');
            followButton.classList.add('btn-dark');
            followerCount.textContent = response.follower_count;
          }
        } else {
          console.error('팔로우 요청 실패');
        }
      };

      // 요청 전송
      xhr.send();
    });
  });
});