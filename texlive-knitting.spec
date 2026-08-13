%global tl_name knitting
%global tl_revision 50782
%global tl_version 3.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Produce knitting charts, in Plain TeX or LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/knitting
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/knitting.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/knitting.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package provides symbol fonts and commands to write charted
instructions for cable and lace knitting patterns, using either plain
TeX or LaTeX. The fonts are available both as Metafont source and in
Adobe Type 1 format.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from knitting:
Map knitfont.map
TL_DROPIN_EOF
