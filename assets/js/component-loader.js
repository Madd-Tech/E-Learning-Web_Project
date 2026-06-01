/**
 * MaddCourse Component Loader
 * Loads reusable HTML components (header, footer) into pages
 * Usage: Add data-component="path/to/component.html" to a div
 */
(function () {
  'use strict';

  /**
   * Detect the base path relative to the current page.
   * Pages in subdirectories (e.g., courses/) need "../" prefix.
   */
  function getBasePath() {
    const path = window.location.pathname;
    const depth = (path.match(/\//g) || []).length - 1;
    // Check if we're in a subdirectory by looking at the script tag src
    const scripts = document.querySelectorAll('script[src*="component-loader"]');
    if (scripts.length > 0) {
      const src = scripts[0].getAttribute('src');
      const prefixMatch = src.match(/^((?:\.\.\/)+)/);
      if (prefixMatch) {
        return prefixMatch[1];
      }
    }
    return '';
  }

  /**
   * Load a component HTML file into a target element
   */
  async function loadComponent(element) {
    const componentPath = element.getAttribute('data-component');
    if (!componentPath) return;

    const basePath = getBasePath();
    const fullPath = basePath + componentPath;

    try {
      const response = await fetch(fullPath);
      if (!response.ok) throw new Error(`Failed to load ${fullPath}: ${response.status}`);
      let html = await response.text();

      // If we're in a subdirectory, fix relative links in the component
      if (basePath) {
        // Fix href links that don't start with http, #, or ../
        html = html.replace(/href="(?!https?:\/\/|#|mailto:|\.\.\/)(.*?)"/g, `href="${basePath}$1"`);
        // Fix src links
        html = html.replace(/src="(?!https?:\/\/|\.\.\/)(.*?)"/g, `src="${basePath}$1"`);
      }

      element.innerHTML = html;

      // After loading header, set active nav link
      if (componentPath.includes('header')) {
        setActiveNavLink();
        initMobileNav();
      }
    } catch (error) {
      console.error('Component Loader Error:', error);
    }
  }

  /**
   * Highlight the current page's nav link
   */
  function setActiveNavLink() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('#navbar a');

    navLinks.forEach(function (link) {
      link.classList.remove('active');
      const href = link.getAttribute('href');
      if (!href) return;

      if (currentPage === 'courses.html' && href === 'courses.html') {
        link.classList.add('active');
      } else if (currentPage.includes('courses/') || window.location.pathname.includes('/courses/')) {
        // We're on a course detail page
        const coursesLink = document.querySelector('#navbar a[href="courses.html"], #navbar a[href="../courses.html"]');
        if (coursesLink) coursesLink.classList.add('active');
      } else if (currentPage === 'index.html' || currentPage === '') {
        if (href === 'index.html#hero' || href === 'index.html') {
          link.classList.add('active');
        }
      }
    });
  }

  /**
   * Re-initialize mobile nav toggle after dynamically loading header
   */
  function initMobileNav() {
    const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
    if (mobileNavToggle) {
      mobileNavToggle.addEventListener('click', function (e) {
        const navbar = document.querySelector('#navbar');
        navbar.classList.toggle('navbar-mobile');
        this.classList.toggle('bi-list');
        this.classList.toggle('bi-x');
      });
    }

    // Mobile nav dropdowns
    document.querySelectorAll('.navbar .dropdown > a').forEach(function (el) {
      el.addEventListener('click', function (e) {
        const navbar = document.querySelector('#navbar');
        if (navbar.classList.contains('navbar-mobile')) {
          e.preventDefault();
          this.nextElementSibling.classList.toggle('dropdown-active');
        }
      });
    });
  }

  /**
   * Initialize: load all components on page
   */
  async function init() {
    const components = document.querySelectorAll('[data-component]');
    const promises = Array.from(components).map(loadComponent);
    await Promise.all(promises);

    // Dispatch event when all components are loaded
    document.dispatchEvent(new Event('componentsLoaded'));
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
