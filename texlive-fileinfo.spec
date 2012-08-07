# revision 26696
# category Package
# catalog-ctan /macros/latex/contrib/fileinfo
# catalog-date 2012-05-28 13:29:39 +0200
# catalog-license lppl1.3
# catalog-version 0.4
Name:		texlive-fileinfo
Version:	0.4
Release:	1
Summary:	Enhanced display of LaTeX File Information
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fileinfo
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fileinfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fileinfo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fileinfo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides two packages, readprov and myfilist. The
readprov package provides a means of reading file information
without loading the body of the file. The myfilist package uses
readprov and controls what \listfiles will report.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fileinfo/fileinfo.RLS
%{_texmfdistdir}/tex/latex/fileinfo/myfilist.sty
%{_texmfdistdir}/tex/latex/fileinfo/readprov.sty
%doc %{_texmfdistdir}/doc/latex/fileinfo/CONTENTs.txt
%doc %{_texmfdistdir}/doc/latex/fileinfo/README
%doc %{_texmfdistdir}/doc/latex/fileinfo/README.pdf
%doc %{_texmfdistdir}/doc/latex/fileinfo/RELEASE.txt
%doc %{_texmfdistdir}/doc/latex/fileinfo/myfilist.pdf
%doc %{_texmfdistdir}/doc/latex/fileinfo/readprov.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fileinfo/README.tex
%doc %{_texmfdistdir}/source/latex/fileinfo/gather.tex
%doc %{_texmfdistdir}/source/latex/fileinfo/myfilist.tex
%doc %{_texmfdistdir}/source/latex/fileinfo/readprov.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
