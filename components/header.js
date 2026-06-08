(function() {
  const isSubdir = window.location.pathname.includes('/courses/');
  const basePath = isSubdir ? '../' : '';

  const template = `
<header id="header" class="fixed-top d-flex align-items-center">
  <div class="container d-flex align-items-center justify-content-between">
    <h1 class="logo"><a href="${basePath}index.html">W3<span style="color: rgba(39, 124, 30, 1); font-weight:bolder;">School</span></a></h1>
    <nav id="navbar" class="navbar">
      <ul>
        <li><a class="nav-link scrollto" href="${basePath}index.html#hero">Home</a></li>
        <li><a class="nav-link scrollto" href="${basePath}index.html#about">About</a></li>
        <li><a class="nav-link scrollto" href="${basePath}index.html#services">Services</a></li>
        <li><a class="nav-link scrollto" href="${basePath}index.html#portfolio">Courses</a></li>
        <li><a class="nav-link scrollto" href="${basePath}index.html#team">Team</a></li>
        <li><a class="nav-link scrollto" href="${basePath}index.html#footer">Contact</a></li>
        <li><a class="getstarted scrollto" href="${basePath}index.html#portfolio">Get Started</a></li>
      </ul>
      <i class="bi bi-list mobile-nav-toggle"></i>
    </nav>
  </div>
</header>
  `;

  document.write(template);

  window.addEventListener('DOMContentLoaded', () => {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('#navbar a');
    navLinks.forEach(link => {
      link.classList.remove('active');
      const href = link.getAttribute('href');
      if (!href) return;
      
      if (currentPage.includes('courses.html') && href.includes('courses.html')) {
        link.classList.add('active');
      } else if (window.location.pathname.includes('/courses/')) {
        if (href.includes('courses.html')) link.classList.add('active');
      } else if (currentPage === 'index.html' || currentPage === '') {
        if (href.includes('index.html#hero') || href === 'index.html' || href === '#hero') {
          link.classList.add('active');
        }
      }
    });
  });
})();
