# Portfolio & Blog Platform Specification

## 1. Project Overview

**Project Name:** Research Portfolio  
**Type:** Personal Portfolio & Blog Platform  
**Core Functionality:** A premium portfolio website for a researcher in power systems and renewable energy integration, featuring blog, projects showcase, and contact system.  
**Target Users:** Academic researchers, industry professionals, potential collaborators

---

## 2. UI/UX Specification

### 2.1 Layout Structure

**Pages:**
- Home (/)
- About (/about/)
- Projects (/projects/, /projects/<slug>/)
- Blog (/blog/, /blog/<slug>/)
- Contact (/contact/)
- Admin (/admin/)

**Header:**
- Fixed navigation bar with glassmorphism effect
- Logo/Name on left
- Navigation links center: Home, About, Projects, Blog, Contact
- Dark mode toggle on right
- Mobile: Hamburger menu

**Footer:**
- Social links (GitHub, LinkedIn, Google Scholar)
- Copyright text
- Quick navigation

### 2.2 Visual Design

**Color Palette:**
- Primary: `#0EA5E9` (Electric Blue / Sky)
- Primary Dark: `#0284C7`
- Secondary: `#10B981` (Emerald Green - Energy theme)
- Accent: `#F59E0B` (Amber)
- Background Light: `#FAFBFC`
- Background Dark: `#0F172A`
- Surface Light: `#FFFFFF`
- Surface Dark: `#1E293B`
- Text Light: `#1F2937`
- Text Dark: `#F1F5F9`
- Muted: `#6B7280`

**Typography:**
- Headings: "Plus Jakarta Sans" (700, 600)
- Body: "Inter" (400, 500, 600)
- Code: "JetBrains Mono"
- H1: 48px / 56px mobile: 36px
- H2: 36px / 44px mobile: 28px
- H3: 24px / 32px mobile: 20px
- Body: 16px / 24px
- Small: 14px / 20px

**Spacing System:**
- Section padding: 80px vertical (mobile: 48px)
- Container max-width: 1280px
- Grid gap: 24px / 32px
- Card padding: 24px
- Border radius: 12px (cards), 8px (buttons), 16px (large elements)

**Visual Effects:**
- Box shadows: `0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)`
- Glassmorphism: `backdrop-blur-lg bg-white/70 dark:bg-slate-900/70`
- Gradients: Primary gradient `bg-gradient-to-r from-sky-500 to-emerald-500`
- Hover transitions: 200ms ease-out
- Page load animations: Fade up with stagger

### 2.3 Responsive Breakpoints
- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

---

## 3. Component Specification

### 3.1 Hero Section (Home)
- Large name with gradient text
- Title: "Researcher in Power Systems & Renewable Energy Integration"
- Short bio (2-3 lines)
- Two CTA buttons: "View Work" (primary), "Contact Me" (outline)
- Animated background with subtle grid pattern + floating particles

### 3.2 About Section
- Profile image (circular, with glow effect)
- Detailed bio text
- Timeline with education/experience
- Skills grid with icons
- Download CV button

### 3.3 Projects Cards
- Featured image (aspect-video)
- Title, description (2-3 lines)
- Technology tags (pills)
- GitHub & Live links
- Hover: lift effect + shadow increase

### 3.4 Blog Cards
- Featured image (aspect-video)
- Title, excerpt (3 lines)
- Tags (max 3)
- Date + reading time
- Hover: subtle scale

### 3.5 Contact Form
- Name, Email, Message fields
- Floating labels
- Validation states
- Submit button with loading state

### 3.6 Navigation
- Active state: underline with gradient
- Hover: color transition
- Mobile: slide-in drawer

---

## 4. Functionality Specification

### 4.1 Blog System
- Rich text content (CKEditor or Quill)
- Auto-generated slugs
- Featured image upload
- Tags (many-to-many)
- Reading time calculation
- Pagination (6 posts per page)
- Search functionality

### 4.2 Projects System
- CRUD operations
- Multiple images (gallery)
- Technology tags
- Featured flag for homepage
- GitHub & Live URLs
- Filter by technology

### 4.3 Contact System
- Form validation
- Save to database
- Success/error messages
- Optional email notification

### 4.4 Profile/About
- Single profile model
- Social links
- CV upload (PDF)
- Skills list
- Timeline entries

### 4.5 Admin Dashboard
- Custom themed (dark sidebar)
- Dashboard with stats cards
- Recent activity feed
- Quick action buttons
- CRUD for all models
- Search & filter
- Image previews

### 4.6 SEO Features
- Meta titles/descriptions
- Open Graph tags
- Sitemap.xml
- Robots.txt
- Semantic HTML

### 4.7 Dark Mode
- Toggle in header
- Persisted in localStorage
- System preference detection
- Smooth transition

---

## 5. Data Models

### Profile
- name: CharField
- title: CharField
- bio: TextField
- profile_image: ImageField
- cv: FileField
- email: EmailField
- github: URLField
- linkedin: URLField
- google_scholar: URLField
- skills: ManyToMany(Skill)

### Skill
- name: CharField
- icon: CharField (optional)
- category: CharField (technical/research)

### Timeline
- title: CharField
- organization: CharField
- description: TextField
- start_date: DateField
- end_date: DateField (nullable)
- is_education: BooleanField

### Project
- title: CharField
- slug: SlugField
- description: TextField
- image: ImageField
- technologies: ManyToMany(Tag)
- github_link: URLField
- live_link: URLField
- featured: BooleanField
- created_at: DateTimeField

### Tag
- name: CharField
- slug: SlugField

### BlogPost
- title: CharField
- slug: SlugField
- content: TextField
- featured_image: ImageField
- tags: ManyToMany(Tag)
- created_at: DateTimeField
- updated_at: DateTimeField
- published: BooleanField

### ContactMessage
- name: CharField
- email: EmailField
- message: TextField
- created_at: DateTimeField
- read: BooleanField

---

## 6. Technical Stack

- Django 4.2+
- SQLite
- Django CKEditor (rich text)
- Tailwind CSS (via CDN for simplicity)
- HTMX (for interactivity)
- Class-based views
- Django crispy forms

---

## 7. Acceptance Criteria

1. ✓ Home page loads with hero, about preview, featured projects, latest blog
2. ✓ About page shows full bio, timeline, skills, CV download
3. ✓ Projects page lists all projects with filtering
4. ✓ Blog paginated with reading time
5. ✓ Contact form saves messages
6. ✓ Custom admin dashboard with stats
7. ✓ Dark mode toggle works
8. ✓ Fully responsive on mobile
9. ✓ Clean, modern, premium aesthetic
10. ✓ No Bootstrap default look
