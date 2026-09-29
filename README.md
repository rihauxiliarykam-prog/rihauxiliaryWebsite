# Royal Inland Hospital Auxiliary Website

A modern, premium-looking website built with plain HTML, CSS, and minimal vanilla JavaScript. This website showcases the RIH Auxiliary's services, volunteer opportunities, and community impact.

## 🚀 Features

- **Modern Design**: Clean, professional layout with premium styling
- **Fully Responsive**: Optimized for all devices (desktop, tablet, mobile)
- **Accessibility**: WCAG compliant with skip links and proper ARIA labels
- **Lightweight**: Fast loading with optimized images and minimal JavaScript
- **Easy to Customize**: Simple HTML structure and CSS classes

## 🛠 How to Edit This Site (read me first)

The root `*.html` files are **built files** — a banner comment at the top of each says so.
The header, nav, footer and font/stylesheet links live in ONE place and are stamped onto
every page by a small script. To make changes:

1. **Page content** → edit `tools/pages/<page>.html`
   (each file holds that page's `<head>` metadata between `<!-- page:head -->` markers,
   followed by its `<main>` content).
2. **Nav, footer, fonts** → edit the templates at the top of `tools/build.py`.
3. **Rebuild** → `python3 tools/build.py` (or `python3 tools/build.py about` for one page).
   Python 3 only, no dependencies, no install step.
4. Commit both the source and the rebuilt root files. Hosting (Cloudflare) serves the
   static files directly — there is no build step in deployment.

Styling lives in `assets/css/site.css` (design tokens at the top, then one commented
section per component). Behaviour lives in `assets/js/site.js` (mobile nav + scroll-in
animations; no dependencies).

## 📁 File Structure

```
Lauren/
├── index.html              # Homepage (BUILT - see tools/)
├── about.html              # About Us page
├── volunteer.html          # Volunteer opportunities
├── thrift.html            # Thrift shop information
├── gift-shop.html         # Gift shop details
├── impact.html            # Community impact showcase
├── contact.html           # Contact form and information
├── assets/
│   ├── css/
│   │   └── site.css            # Main stylesheet
│   ├── js/
│   │   └── site.js             # Mobile menu and header behaviour
│   └── images/
│       ├── RIH_emblem main.png # Logo
│       ├── Updated Photos/     # High-quality images
│       └── Thrift & Group photos # Additional images
├── tools/
│   ├── build.py            # Stamps shared header/footer onto every page
│   └── pages/              # SOURCE for each page - edit these, then rebuild
└── README.md
```

## 🎨 Design Features

### Color Palette
Taken from the Auxiliary emblem:
- **Primary**: Navy (#1d4c9a), deep navy (#13305f) for the call-to-action panels
- **Accent**: Warm orange (#f39a3d), used sparingly for small details
- **Neutral**: Ink (#0f1b33) for headings, warm paper (#faf8f4) and sand (#f3efe7) backgrounds

### Typography
- **Headings**: Newsreader serif (Google Fonts)
- **Body**: The device's system font (San Francisco on Apple devices, Segoe UI on Windows)
- **Hierarchy**: Clear size and weight variations

### Layout
- **Grid System**: Flexible CSS Grid layouts
- **Cards**: Consistent card components
- **Spacing**: Balanced margins and padding
- **Shadows**: Subtle depth and dimension

## 📱 Responsive Design

The website automatically adapts to different screen sizes:

- **Desktop**: Full layout with side-by-side content
- **Tablet**: Adjusted grid layouts
- **Mobile**: Single-column layout with mobile navigation

## 🛠️ Customization Guide

### Changing Colors
Edit the CSS variables at the top of `assets/css/site.css`:

```css
:root {
  --navy: #1d4c9a;      /* Main brand color */
  --orange: #f39a3d;    /* Accent color */
  --paper: #faf8f4;     /* Page background */
}
```

### Updating Content
1. **Text**: Edit the HTML files directly
2. **Images**: Replace images in `assets/images/` folder
3. **Links**: Update navigation and internal links
4. **Contact Info**: Modify contact details in footer

### Adding New Pages
1. Copy an existing HTML file
2. Update the title, meta description, and content
3. Add the page to navigation menus
4. Update the active state in navigation

### Modifying Styles
- **Layout**: Adjust CSS Grid properties
- **Components**: Modify card, button, and form styles
- **Typography**: Change font sizes and weights
- **Spacing**: Update CSS custom properties

## 🔧 Technical Details

### Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- IE11+ (with some limitations)

### Performance
- Optimized images (JPEG format)
- Minimal JavaScript
- CSS custom properties for maintainability
- No external dependencies

### Accessibility
- Semantic HTML structure
- ARIA labels and roles
- Keyboard navigation support
- Screen reader friendly
- High contrast ratios

## 📸 Image Guidelines

### Recommended Image Sizes
- **Hero Images**: 1200x800px
- **Card Images**: 600x400px
- **Gallery Images**: 600x400px
- **Logo**: 80x80px (2x for retina)

### Image Formats
- **JPEG**: For photographs and complex images
- **PNG**: For logos and images with transparency
- **WebP**: Modern format with better compression (optional)

## 🚀 Deployment

### Local Development
1. Open any HTML file in a web browser
2. Use a local server for testing (recommended)
3. No build process required

### Web Hosting
1. Upload all files to your web server
2. Ensure proper file permissions
3. Test all pages and functionality
4. Verify mobile responsiveness

### CDN (Optional)
- Host images on a CDN for better performance
- Update image paths in HTML files
- Consider using WebP format with fallbacks

## 📞 Support

For questions about the website structure or customization:

1. Check the HTML comments for guidance
2. Review the CSS custom properties
3. Test changes in multiple browsers
4. Validate HTML and CSS

## 📝 License

This website template is created for the Royal Inland Hospital Afternoon Auxiliary. Feel free to adapt and modify for your organization's needs.

## 🔄 Updates

To keep the website current:

1. **Regular Reviews**: Check content accuracy monthly
2. **Image Updates**: Refresh photos quarterly
3. **Performance**: Monitor loading times
4. **Accessibility**: Test with screen readers
5. **Mobile**: Test on various devices

---

**Built with ❤️ for community service and healthcare excellence** 