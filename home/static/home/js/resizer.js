$(function() {
  var setRotated = function(argument) {

    $(".bowknot").each(function() {
      var boxHeight = $(this).closest(".box").height();
      $(this).height(boxHeight + 40);
    });

    $(".rotatedText").each(function() {
      var boxHeight = $(this).closest(".box").height();
      var thisHeight = $(this).width();
      $(this).attr('style', 'margin-top:' + (boxHeight / 2 + 20 + thisHeight / 2) + 'px');
    });

  };
  setRotated();
  setInterval(setRotated, 500);
});
