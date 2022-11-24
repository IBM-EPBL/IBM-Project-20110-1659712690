let modalBtns = [...document.querySelectorAll(".apply_button")];
      modalBtns.forEach(function (btn) {
        btn.onclick = function () {
          let apply_modal = btn.getAttribute("data-modal");
          document.getElementById(apply_modal).style.display = "block";
        };
      });
      let closeBtns = [...document.querySelectorAll(".apply_close")];
      closeBtns.forEach(function (btn) {
        btn.onclick = function () {
          let apply_modal = btn.closest(".apply_modal");
          apply_modal.style.display = "none";
        };
      });
      window.onclick = function (event) {
        if (event.target.className === "apply_modal") {
          event.target.style.display = "none";
        }
      };