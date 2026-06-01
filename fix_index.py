import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The new portfolio section
new_portfolio = """    <!-- ======= Portfolio Section ======= -->
    <section id="portfolio" class="portfolio">
      <div class="container">

        <div class="section-title">
          <h2>Courses</h2>
          <p>Courses are the heart of MaddCourse. We offer a variety of courses to help you achieve your goals.</p>
        </div>

        <div class="row">
          <div class="col-lg-12 d-flex justify-content-center">
            <ul id="portfolio-flters">
              <li data-filter="*" class="filter-active">All</li>
              <li data-filter=".filter-web-dev">Web Development</li>
              <li data-filter=".filter-python">Python Programming</li>
              <li data-filter=".filter-data-science">Data Science & Machine Learning</li>
              <li data-filter=".filter-ai">AI Engineering</li>
              <li data-filter=".filter-mobile-app">Mobile App Development</li>
              <li data-filter=".filter-ui-ux">UI/UX</li>
            </ul>
          </div>
        </div>

        <div class="row portfolio-container">

          <div class="col-lg-4 col-md-6 portfolio-item filter-web-dev">
            <div class="portfolio-wrap">
              <img src="assets/img/portfolio/Web_Development.jpg" class="img-fluid" alt="">
              <div class="portfolio-info">
                <h4>Web Development Fundamental</h4>
                <p>Web Development</p>
                <div class="portfolio-links">
                  <a href="assets/img/portfolio/Web_Development.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox" title="Web Development"><i class="bx bx-plus"></i></a>
                  <a href="portfolio-details.html" title="More Details"><i class="bx bx-link"></i></a>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 portfolio-item filter-web-dev">
            <div class="portfolio-wrap">
              <img src="assets/img/portfolio/portfolio-2.jpg" class="img-fluid" alt="">
              <div class="portfolio-info">
                <h4>Laravel Framework</h4>
                <p>Web Development</p>
                <div class="portfolio-links">
                  <a href="assets/img/portfolio/portfolio-2.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox" title="Laravel Framework"><i class="bx bx-plus"></i></a>
                  <a href="portfolio-details.html" title="More Details"><i class="bx bx-link"></i></a>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 portfolio-item filter-python">
            <div class="portfolio-wrap">
              <img src="assets/img/portfolio/Python development Company.jpg" class="img-fluid" alt="">
              <div class="portfolio-info">
                <h4>Python for Beginners</h4>
                <p>Python Programming</p>
                <div class="portfolio-links">
                  <a href="assets/img/portfolio/Python development Company.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox" title="Python for Beginners"><i class="bx bx-plus"></i></a>
                  <a href="portfolio-details.html" title="More Details"><i class="bx bx-link"></i></a>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 portfolio-item filter-data-science">
            <div class="portfolio-wrap">
              <img src="assets/img/portfolio/Data_Science.jpg" class="img-fluid" alt="">
              <div class="portfolio-info">
                <h4>Data Science for Beginners</h4>
                <p>Data Science & Machine Learning</p>
                <div class="portfolio-links">
                  <a href="assets/img/portfolio/Data_Science.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox" title="Data Science for Beginners"><i class="bx bx-plus"></i></a>
                  <a href="portfolio-details.html" title="More Details"><i class="bx bx-link"></i></a>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 portfolio-item filter-ai">
            <div class="portfolio-wrap">
              <img src="assets/img/portfolio/AI_Engineering.jpg" class="img-fluid" alt="">
              <div class="portfolio-info">
                <h4>Introduction to AI & Generative AI</h4>
                <p>AI Engineering</p>
                <div class="portfolio-links">
                  <a href="assets/img/portfolio/AI_Engineering.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox" title="Introduction to AI"><i class="bx bx-plus"></i></a>
                  <a href="portfolio-details.html" title="More Details"><i class="bx bx-link"></i></a>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 portfolio-item filter-mobile-app">
            <div class="portfolio-wrap">
              <img src="assets/img/portfolio/portfolio-6.jpg" class="img-fluid" alt="">
              <div class="portfolio-info">
                <h4>Mobile App with Flutter</h4>
                <p>Mobile App Development</p>
                <div class="portfolio-links">
                  <a href="assets/img/portfolio/portfolio-6.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox" title="Mobile App with Flutter"><i class="bx bx-plus"></i></a>
                  <a href="portfolio-details.html" title="More Details"><i class="bx bx-link"></i></a>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 portfolio-item filter-ui-ux">
            <div class="portfolio-wrap">
              <img src="assets/img/portfolio/portfolio-7.jpg" class="img-fluid" alt="">
              <div class="portfolio-info">
                <h4>UI/UX Masterclass</h4>
                <p>UI/UX</p>
                <div class="portfolio-links">
                  <a href="assets/img/portfolio/portfolio-7.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox" title="UI/UX Masterclass"><i class="bx bx-plus"></i></a>
                  <a href="portfolio-details.html" title="More Details"><i class="bx bx-link"></i></a>
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section><!-- End Portfolio Section -->"""

pattern = r'<!-- ======= Portfolio Section ======= -->\s*<section id="portfolio" class="portfolio">.*?</section><!-- End Portfolio Section -->'

new_html = re.sub(pattern, new_portfolio, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("index.html fixed!")
