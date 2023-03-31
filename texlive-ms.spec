Name:		texlive-ms
Version:	57473
Release:	2
Summary:	Various LaTeX packages by Martin Schroder
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ms
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ms.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ms.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ms.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/ms
%doc %{_texmfdistdir}/doc/latex/ms
#- source
%doc %{_texmfdistdir}/source/latex/ms

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
