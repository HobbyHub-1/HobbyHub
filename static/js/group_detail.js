const form = document.querySelector('#likes-form');
    const heartIcon = document.querySelector('#group-heart');

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      const groupId = event.target.dataset.groupId;
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

      axios({
        method: 'post',
        url: `/posts/group/${groupId}/group_likes/`,
        headers: { 'X-CSRFToken': csrftoken },
      })
        .then((response) => {
          const isLiked = response.data.is_liked;
          if (isLiked) {
            heartIcon.classList.remove('bi-heart');
            heartIcon.classList.add('bi-heart-fill');
          } else {
            heartIcon.classList.remove('bi-heart-fill');
            heartIcon.classList.add('bi-heart');
          }
        })
        .catch((error) => {
          console.error(error);
        });
    });
