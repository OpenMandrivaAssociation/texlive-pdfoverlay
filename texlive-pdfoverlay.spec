Name:		texlive-pdfoverlay
Version:	64210
Release:	2
Summary:	A LaTeX style for overlaying text on a PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfoverlay
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfoverlay.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfoverlay.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfoverlay.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
It is often desirable to take an exisiting PDF and easily add
annotations or text overlaying the PDF. This might arise if you
wish to add comments to a PDF, fill in a PDF form, or add text
to a PDF where space has been left for notes. This package
provides a simple interface to do this without having to resort
to inserting one page at a time. Some or all of the pages of
the PDF can be included and not all pages of the PDF need have
overlayed text. It is also possible to include text between
pages of the PDF. Another advantage of this package is that the
overlayed text can be set as normal flowing from one page to
another or with manual page breaks if you wish. It is also
possible to use any standard method to position text at
arbitrary places on a given page.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pdfoverlay
%{_texmfdistdir}/tex/latex/pdfoverlay
%doc %{_texmfdistdir}/doc/latex/pdfoverlay

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
