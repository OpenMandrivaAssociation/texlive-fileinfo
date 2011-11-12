# revision 21259
# category Package
# catalog-ctan /macros/latex/contrib/fileinfo
# catalog-date 2011-02-01 07:24:26 +0100
# catalog-license lppl1.3
# catalog-version 0.3(a)
Name:		texlive-fileinfo
Version:	0.3a
Release:	1
Summary:	Get file information without loading the file
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The bundle provides two packages, readprov and myfilist. The
readprov package provides a means of reading file information
without loading the body of the file. The myfilist package uses
readprov and controls what \listfiles will report.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fileinfo/myfilist.sty
%{_texmfdistdir}/tex/latex/fileinfo/readprov.sty
%doc %{_texmfdistdir}/doc/latex/fileinfo/CONTENTs.txt
%doc %{_texmfdistdir}/doc/latex/fileinfo/README
%doc %{_texmfdistdir}/doc/latex/fileinfo/README.pdf
%doc %{_texmfdistdir}/doc/latex/fileinfo/README.txt
%doc %{_texmfdistdir}/doc/latex/fileinfo/RELEASE.txt
%doc %{_texmfdistdir}/doc/latex/fileinfo/gather.tex
%doc %{_texmfdistdir}/doc/latex/fileinfo/myfilist.pdf
%doc %{_texmfdistdir}/doc/latex/fileinfo/readprov.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fileinfo/README.tex
%doc %{_texmfdistdir}/source/latex/fileinfo/makedoc.cfg
%doc %{_texmfdistdir}/source/latex/fileinfo/myfilist.tex
%doc %{_texmfdistdir}/source/latex/fileinfo/readprov.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
