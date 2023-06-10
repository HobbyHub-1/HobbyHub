  window.addEventListener('scroll', function() {
    var header = document.querySelector('header');
    var nav = document.querySelector('header > nav');
    var scrollPos = window.scrollY;
  
    if (scrollPos > 0) {
      header.style.top = '-50px'; 
      nav.style.top = '-50px'; 
    } else {
      header.style.top = '0';
      nav.style.top = '0';
    }
  });

