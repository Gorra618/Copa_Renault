$(function() {
  var $headline = $('.headline'),
      $inner = $('.inner'),
      $nav = $('nav'),
      navHeight = 75;

  function handleScroll() {
    var scrollTop = $(window).scrollTop(),
        headlineHeight = $headline.outerHeight() - navHeight;

    $headline.css({
      'opacity': (1 - scrollTop / headlineHeight)
    });
    $inner.children().css({
      'transform': 'translateY('+ scrollTop * 0.4 +'px)'
    });

    // Oscurecer navbar al hacer scroll
    if (scrollTop > 0) {
      $nav.addClass('scrolled');
    } else {
      $nav.removeClass('scrolled');
    }
  }

  $(window).on('scroll', handleScroll);
  handleScroll(); // Ejecuta al cargar por si ya está scrolleado
});