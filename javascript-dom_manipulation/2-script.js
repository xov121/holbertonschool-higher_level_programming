document.addEventListener('DOMContentLoaded', function () {
  const redHeader = document.querySelector('#red_header');
  redHeader.addEventListener('click', function () {
    document.querySelector('header').classList.add('red');
  });
});
