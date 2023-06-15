const form = document.querySelector( '#group-likes-form' );

form.addEventListener('submit', function (event) {
  event.preventDefault();
  var csrftoken = document.querySelector( `[name=csrfmiddlewaretoken]` ).value;
  const groupId = event.target.dataset.groupId;

  axios({
    method: 'post',
    url: `/posts/group/${groupId}/group_likes/`,
    headers: { 'X-CSRFToken': csrftoken },
  })
  .then( ( response ) => {
    const isLiked = response.data.is_liked;
    const heartIcon = document.querySelector('#group-heart');
    if (isLiked === true) {
      heartIcon.classList.remove('bi-heart');
      heartIcon.classList.add('bi-heart-fill');
    } else {
      heartIcon.classList.remove('bi-heart-fill');
      heartIcon.classList.add('bi-heart');
    }
    const likeCountTag = document.querySelector('#like-count')
    const likeCountData = response.data.like_count
    likeCountTag.textContent = likeCountData
  })
  .catch((error) => {
    console.log(error);
  });
});
