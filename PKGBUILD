# Maintainer: Your Name <you@example.com>
pkgname=gman
pkgver=0.1.0
pkgrel=1
pkgdesc="AI-powered CLI ‘man’ tool using BitNet (via HuggingFace Transformers + PyTorch)"
arch=('any')
url="https://github.com/yourusername/gman"
license=('MIT')
depends=(
  python
  python-typer
  python-pytorch
  python-transformers
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
  git
)
provides=('gman')
conflicts=('gman')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/yourusername/gman/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('SKIP')  # replace with actual checksum

package() {
  cd "${pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
  python -m installer --destdir="$pkgdir" dist/*.whl
}