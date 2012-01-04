# revision 19595
# category Package
# catalog-ctan /fonts/knitting
# catalog-date 2010-08-29 22:20:17 +0200
# catalog-license lppl1.3
# catalog-version 2.0
Name:		texlive-knitting
Version:	2.0
Release:	2
Summary:	Produce knitting charts, in Plain TeX or LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/knitting
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knitting.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knitting.doc.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/knitting/knitg_sc_in.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitg_sc_out.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitgg.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitgn.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitgp.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitn_sc_in.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitn_sc_out.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitnl.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitnn.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitnp.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitnr.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitw_sc_in.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitw_sc_out.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitwg.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitwn.afm
%{_texmfdistdir}/fonts/afm/public/knitting/knitwp.afm
%{_texmfdistdir}/fonts/map/dvips/knitting/knitfont.map
%{_texmfdistdir}/fonts/source/public/knitting/knit_dimens.mf
%{_texmfdistdir}/fonts/source/public/knitting/knit_grid_cables.mf
%{_texmfdistdir}/fonts/source/public/knitting/knit_nogrid_cables.mf
%{_texmfdistdir}/fonts/source/public/knitting/knit_symbols.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitg_sc_in.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitg_sc_out.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitgg.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitgn.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitgp.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitn_sc_in.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitn_sc_out.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitnl.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitnn.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitnp.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitnr.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitw_sc_in.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitw_sc_out.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitwg.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitwn.mf
%{_texmfdistdir}/fonts/source/public/knitting/knitwp.mf
%{_texmfdistdir}/fonts/tfm/public/knitting/knitg_sc_in.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitg_sc_out.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitgg.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitgn.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitgp.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitn_sc_in.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitn_sc_out.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitnl.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitnn.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitnp.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitnr.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitw_sc_in.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitw_sc_out.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitwg.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitwn.tfm
%{_texmfdistdir}/fonts/tfm/public/knitting/knitwp.tfm
%{_texmfdistdir}/fonts/type1/public/knitting/knitg_sc_in.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitg_sc_out.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitgg.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitgn.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitgp.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitn_sc_in.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitn_sc_out.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitnl.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitnn.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitnp.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitnr.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitw_sc_in.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitw_sc_out.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitwg.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitwn.pfb
%{_texmfdistdir}/fonts/type1/public/knitting/knitwp.pfb
%{_texmfdistdir}/tex/latex/knitting/knitting.sty
%{_texmfdistdir}/tex/latex/knitting/uknit.fd
%{_texmfdistdir}/tex/plain/knitting/knitting.tex
%doc %{_texmfdistdir}/doc/fonts/knitting/README
%doc %{_texmfdistdir}/doc/fonts/knitting/knitexamples.tex
%doc %{_texmfdistdir}/doc/fonts/knitting/knitkey.tex
%doc %{_texmfdistdir}/doc/fonts/knitting/knitting-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/knitting/knitting-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
