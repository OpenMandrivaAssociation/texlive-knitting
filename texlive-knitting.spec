Name:		texlive-knitting
Version:	50782
Release:	2
Summary:	Produce knitting charts, in Plain TeX or LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/knitting
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knitting.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knitting.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides symbol fonts and commands to write charted
instructions for cable and lace knitting patterns, using either
plain TeX or LaTeX. The fonts are available both as MetaFont
source and in Adobe Type 1 format.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/knitting
%{_texmfdistdir}/fonts/map/dvips/knitting
%{_texmfdistdir}/fonts/source/public/knitting
%{_texmfdistdir}/fonts/tfm/public/knitting
%{_texmfdistdir}/fonts/type1/public/knitting
%{_texmfdistdir}/tex/latex/knitting
%{_texmfdistdir}/tex/plain/knitting
%doc %{_texmfdistdir}/doc/fonts/knitting

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
