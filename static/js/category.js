var likeforms = document.querySelectorAll( `.HHlike-form` );
var csrftoken = document.querySelector( `[name=csrfmiddlewaretoken]` ).value;

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
      const heartIcon = form.querySelector( `#post-heart-${postId}`);
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