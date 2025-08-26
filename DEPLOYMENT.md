# Data Trust Engineering - Deployment Guide

## Overview
This guide covers deploying the Data Trust Engineering (DTE) project to GitHub Pages and configuring your custom domain.

## Local Development

### Prerequisites
- Python 3.8+
- Hugo (latest extended version)
- Git

### Running Locally

#### 1. Trust Dashboard (Streamlit)
```bash
cd tools/data-trust-dashboard
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
Access at: http://localhost:8501

#### 2. Hugo Site
```bash
# From project root
hugo server --bind 0.0.0.0 --port 1313
```
Access at: http://localhost:1313

## GitHub Pages Deployment

### 1. Enable GitHub Pages
1. Go to your repository: `https://github.com/askbrianfx/DataTrustEngineering`
2. Navigate to **Settings** → **Pages**
3. Set **Source** to "GitHub Actions"
4. Ensure the repository is public (required for free GitHub Pages)

### 2. Automatic Deployment
The repository includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that automatically:
- Builds the Hugo site on every push to `main`
- Deploys to GitHub Pages
- Handles Hugo dependencies and optimization

### 3. Manual Deployment
If you need to deploy manually:
```bash
# Build the site
hugo --minify

# The built site will be in the `public/` directory
# GitHub Actions will handle the deployment automatically
```

## Custom Domain Configuration

### Option 1: datatrustmanifesto.org (Current)
1. **Update config.toml**:
   ```toml
   baseURL = "https://datatrustmanifesto.org"
   ```

2. **Add CNAME file**:
   Create `static/CNAME` with content:
   ```
   datatrustmanifesto.org
   ```

3. **DNS Configuration**:
   - Add CNAME record: `datatrustmanifesto.org` → `datatrustengineering.github.io`
   - Or A records pointing to GitHub Pages IPs

### Option 2: Alternative Domain (Future)
1. **Update config.toml**:
   ```toml
   baseURL = "https://yourdomain.com"
   ```

2. **Add CNAME file**:
   Create `static/CNAME` with content:
   ```
   yourdomain.com
   ```

### Option 3: GitHub Pages Subdomain
Keep current configuration:
```toml
baseURL = "https://askbrianfx.github.io"
```

## Post-Deployment Verification

### 1. Check GitHub Actions
- Go to **Actions** tab in your repository
- Verify the deployment workflow completed successfully
- Check for any build errors

### 2. Test the Site
- Visit your deployed URL
- Test all navigation links
- Verify the Trust Dashboard loads correctly
- Check mobile responsiveness

### 3. Test Trust Dashboard
- Ensure the HTML version loads properly
- Verify all charts render correctly
- Test the Streamlit app (if deployed separately)

## Troubleshooting

### Common Issues

#### Hugo Build Errors
```bash
# Clear Hugo cache
hugo --gc

# Check Hugo version
hugo version

# Verify theme dependencies
hugo mod get -u
```

#### GitHub Pages Not Updating
- Check GitHub Actions for build failures
- Verify the `main` branch has the latest changes
- Wait 5-10 minutes for changes to propagate

#### Custom Domain Issues
- Verify DNS records are correct
- Check CNAME file in the `static/` directory
- Ensure domain is properly configured in GitHub Pages settings

### Getting Help
- Check GitHub Actions logs for detailed error messages
- Review Hugo documentation for build issues
- Open an issue in the repository for persistent problems

## Next Steps

### Phase 2: Community Activation
- [ ] Deploy to GitHub Pages
- [ ] Configure custom domain
- [ ] Test all functionality
- [ ] Share with initial community members

### Phase 3: Content Expansion
- [ ] Add real case studies
- [ ] Complete use case examples
- [ ] Build contributor base

## Security Notes
- The repository is public (required for GitHub Pages)
- No sensitive data should be committed
- Use environment variables for any API keys
- Review all content before deployment

---

**Last Updated**: January 2025  
**Maintainer**: Data Trust Engineering Team
