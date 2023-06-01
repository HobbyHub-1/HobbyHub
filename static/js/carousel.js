var slides = document.querySelectorAll('.slide');
var prevButton = document.querySelector('.prev-button');
var nextButton = document.querySelector('.next-button');
var dots = document.querySelectorAll('.dot');

var currentIndex = 0;
var timer = setInterval(nextSlide, 10000);

function showSlide(index) {
  // 현재 슬라이드 표시
  slides.forEach(function (slide) {
    slide.style.display = 'none';
  });
  slides[index].style.display = 'block';

  // 현재 도트 표시
  dots.forEach(function (dot) {
    dot.classList.remove('active');
  });
  dots[index].classList.add('active');
}

function prevSlide() {
  currentIndex = (currentIndex - 1 + slides.length) % slides.length;
  showSlide(currentIndex);
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % slides.length;
  showSlide(currentIndex);
}

function goToSlide(index) {
  currentIndex = index;
  showSlide(currentIndex);
}

prevButton.addEventListener('click', prevSlide);
nextButton.addEventListener('click', nextSlide);

dots.forEach(function (dot, index) {
  dot.addEventListener('click', function () {
    goToSlide(index);
  });
});

// 슬라이드 쇼 자동 재생 제어
function startTimer() {
  timer = setInterval(nextSlide, 10000);
}

function stopTimer() {
  clearInterval(timer);
}

document.querySelector('.carousel').addEventListener('mouseover', stopTimer);
document.querySelector('.carousel').addEventListener('mouseout', startTimer);

// 초기 슬라이드 표시
showSlide(currentIndex);
