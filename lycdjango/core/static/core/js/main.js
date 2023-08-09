(function ($) {
  "use strict";

  // Dropdown on mouse hover
  $(document).ready(function () {
    function toggleNavbarMethod() {
      if ($(window).width() > 768) {
        $(".navbar .dropdown")
          .on("mouseover", function () {
            $(".dropdown-toggle", this).trigger("click");
          })
          .on("mouseout", function () {
            $(".dropdown-toggle", this).trigger("click").blur();
          });
      } else {
        $(".navbar .dropdown").off("mouseover").off("mouseout");
      }
    }
    toggleNavbarMethod();
    $(window).resize(toggleNavbarMethod);
  });

  // Product Details Slider
  const productSlider = new bootstrap.Carousel(
    document.getElementById("product-slider")
  );

   // Hacer que el carrusel se mueva automáticamente
   $('.carousel').carousel({
    interval: 3000 // Ajusta el intervalo de tiempo en milisegundos (3 segundos en este caso)
  });
  
  // Evento para pausar el carrusel al interactuar con él
  productSlider.pause();

  // Evento para cambiar el slide activo al hacer clic en las miniaturas
  const sliderNavItems = document.querySelectorAll(".slider-nav-img");
  sliderNavItems.forEach((item, index) => {
    item.addEventListener("click", () => {
      productSlider.to(index); // Cambiar al slide correspondiente
      productSlider.cycle(); // Reiniciar la reproducción automática
    });
  });

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $(".back-to-top").fadeIn("slow");
    } else {
      $(".back-to-top").fadeOut("slow");
    }
  });
  $(".back-to-top").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1500, "easeInOutExpo");
    return false;
  });

//   // Quantity
//   $(".qty button").on("click", function () {
//     var $button = $(this);
//     var oldValue = $button.parent().find("input").val();
//     if ($button.hasClass("btn-plus")) {
//         var newVal = parseFloat(oldValue) + 1;
//     } else {
//         if (oldValue > 0) {
//             var newVal = parseFloat(oldValue) - 1;
//         } else {
//             newVal = 0;
//         }
//     }
//     $button.parent().find("input").val(newVal);
// });

  // Shipping address show hide
  $(".checkout #shipto").change(function () {
    if ($(this).is(":checked")) {
      $(".checkout .shipping-address").slideDown();
    } else {
      $(".checkout .shipping-address").slideUp();
    }
  });

  // Payment methods show hide
  $(".checkout .payment-method .custom-control-input").change(function () {
    if ($(this).prop("checked")) {
      var checkbox_id = $(this).attr("id");
      $(".checkout .payment-method .payment-content").slideUp();
      $("#" + checkbox_id + "-show").slideDown();
    }
  });
})(jQuery);
