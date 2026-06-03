(function() {
  const isSubdir = window.location.pathname.includes('/courses/');
  const basePath = isSubdir ? '../' : '';

  const template = `
<footer id="footer">
  <div class="footer-top">
    <div class="container">
      <div class="row">
        <div class="col-lg-3 col-md-6">
          <div class="footer-info">
            <h3>W3<span style="color: rgba(39, 124, 30, 1);">School</span></h3>
            <p>
              A108 Adam Street <br>
              NY 535022, USA<br><br>
              <strong>Phone:</strong> +1 5589 55488 55<br>
              <strong>Email:</strong> info@maddcourse.com<br>
            </p>
            <div class="social-links mt-3">
              <a href="https://www.youtube.com/@w3schools" class="youtube"><i class="bx bxl-youtube"></i></a>
              <a href="https://www.facebook.com/w3schools" class="facebook"><i class="bx bxl-facebook"></i></a>
              <a href="https://www.instagram.com/w3schools.com_official/" class="instagram"><i class="bx bxl-instagram"></i></a>
              <a href="https://discord.com/invite/w3schools" class="discord"><i class="bx bxl-discord"></i></a>
              <a href="https://www.linkedin.com/company/w3schools.com/" class="linkedin"><i class="bx bxl-linkedin"></i></a>
            </div>
          </div>
        </div>

        <div class="col-lg-2 col-md-6 footer-links">
          <h4>Useful Links</h4>
          <ul>
            <li><i class="bx bx-chevron-right"></i> <a href="${basePath}index.html">Home</a></li>
            <li><i class="bx bx-chevron-right"></i> <a href="${basePath}index.html#about">About us</a></li>
            <li><i class="bx bx-chevron-right"></i> <a href="${basePath}courses.html">Courses</a></li>
            <li><i class="bx bx-chevron-right"></i> <a href="#">Terms of service</a></li>
            <li><i class="bx bx-chevron-right"></i> <a href="#">Privacy policy</a></li>
          </ul>
        </div>

        <div class="col-lg-3 col-md-6 footer-links">
          <h4>Our Courses</h4>
          <ul>
            <li><i class="bx bx-chevron-right"></i> <a href="${basePath}courses/web-development.html">Web Development</a></li>
            <li><i class="bx bx-chevron-right"></i> <a href="${basePath}courses/python-programming.html">Python Programming</a></li>
            <li><i class="bx bx-chevron-right"></i> <a href="${basePath}courses/data-science.html">Data Science</a></li>
            <li><i class="bx bx-chevron-right"></i> <a href="${basePath}courses/mobile-app-development.html">Mobile Apps</a></li>
            <li><i class="bx bx-chevron-right"></i> <a href="${basePath}courses/ai-engineering.html">AI Engineering</a></li>
          </ul>
        </div>

      </div>
    </div>
  </div>

  <div class="container">
    <div class="copyright">
      &copy; Copyright <strong><span>W3School</span></strong>. All Rights Reserved
    </div>
    <div class="credits">
      Develop by <a href="https://bootstrapmade.com/">khrllhmr</a>
    </div>
  </div>
</footer>
  `;

  document.write(template);
})();
