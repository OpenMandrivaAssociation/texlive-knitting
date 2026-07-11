%global tl_name knitting
%global tl_revision 50782

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	Produce knitting charts, in Plain TeX or LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/knitting
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/knitting.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/knitting.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides symbol fonts and commands to write charted
instructions for cable and lace knitting patterns, using either plain
TeX or LaTeX. The fonts are available both as Metafont source and in
Adobe Type 1 format.

