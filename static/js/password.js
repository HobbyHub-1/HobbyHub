  function handleFormSubmit(event) {
    event.preventDefault(); // 기본 제출 동작을 막음
    var form = event.target; // 이벤트가 발생한 폼 요소를 가져옴
    
    // 폼 데이터를 서버로 전송하는 AJAX 요청을 수행
    fetch(form.action, {
      method: form.method,
      body: new FormData(form),
    })
    .then(function(response) {
      if (response.ok) {
        // 변경 사항이 성공적으로 저장되면 모달을 보여줌
        var modal = document.getElementById('exampleModal');
        var modalInstance = bootstrap.Modal.getInstance(modal);
        modalInstance.show();
      } else {
        // 저장에 실패한 경우에 대한 처리
        alert('저장 실패');
      }
    })
    .catch(function(error) {
      console.error('오류 발생:', error);
    });
  }

  // 폼 제출 이벤트를 감지하고 처리하는 리스너 등록
  var passwordChangeForm = document.getElementById('CustomPasswordChangeForm');
  passwordChangeForm.addEventListener('submit', handleFormSubmit);

