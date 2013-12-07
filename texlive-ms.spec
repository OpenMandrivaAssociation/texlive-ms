# revision 29849
# category Package
# catalog-ctan /macros/latex/contrib/ms
# catalog-date 2012-05-24 17:58:39 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-ms
Version:	20120524
Release:	2
Summary:	Various LaTeX packages by Martin Schroder
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ms
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ms.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ms.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ms.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A bundle of LaTeX packages by Martin Schroder; the collection
comprises: - count1to, make use of fixed TeX counters; -
everysel, set commands to execute every time a font is
selected; - everyshi, set commands to execute whenever a page
is shipped out; - multitoc, typeset the table of contents in
multiple columns; - prelim2e, mark typeset pages as
preliminary; and - ragged2e, typeset ragged text and allow
hyphenation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ms/count1to.sty
%{_texmfdistdir}/tex/latex/ms/everysel.sty
%{_texmfdistdir}/tex/latex/ms/everyshi.sty
%{_texmfdistdir}/tex/latex/ms/multitoc.sty
%{_texmfdistdir}/tex/latex/ms/prelim2e.sty
%{_texmfdistdir}/tex/latex/ms/ragged2e.sty
%doc %{_texmfdistdir}/doc/latex/ms/count1to.pdf
%doc %{_texmfdistdir}/doc/latex/ms/everysel.pdf
%doc %{_texmfdistdir}/doc/latex/ms/everyshi.asc
%doc %{_texmfdistdir}/doc/latex/ms/everyshi.bug
%doc %{_texmfdistdir}/doc/latex/ms/everyshi.pdf
%doc %{_texmfdistdir}/doc/latex/ms/multitoc.asc
%doc %{_texmfdistdir}/doc/latex/ms/multitoc.bug
%doc %{_texmfdistdir}/doc/latex/ms/multitoc.pdf
%doc %{_texmfdistdir}/doc/latex/ms/prelim2e.pdf
%doc %{_texmfdistdir}/doc/latex/ms/ragged2e.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ms/count1to.drv
%doc %{_texmfdistdir}/source/latex/ms/count1to.dtx
%doc %{_texmfdistdir}/source/latex/ms/count1to.ins
%doc %{_texmfdistdir}/source/latex/ms/everysel.drv
%doc %{_texmfdistdir}/source/latex/ms/everysel.dtx
%doc %{_texmfdistdir}/source/latex/ms/everysel.ins
%doc %{_texmfdistdir}/source/latex/ms/everyshi.drv
%doc %{_texmfdistdir}/source/latex/ms/everyshi.dtx
%doc %{_texmfdistdir}/source/latex/ms/everyshi.ins
%doc %{_texmfdistdir}/source/latex/ms/multitoc.drv
%doc %{_texmfdistdir}/source/latex/ms/multitoc.dtx
%doc %{_texmfdistdir}/source/latex/ms/multitoc.ins
%doc %{_texmfdistdir}/source/latex/ms/prelim2e.drv
%doc %{_texmfdistdir}/source/latex/ms/prelim2e.dtx
%doc %{_texmfdistdir}/source/latex/ms/prelim2e.ins
%doc %{_texmfdistdir}/source/latex/ms/ragged2e.drv
%doc %{_texmfdistdir}/source/latex/ms/ragged2e.dtx
%doc %{_texmfdistdir}/source/latex/ms/ragged2e.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
