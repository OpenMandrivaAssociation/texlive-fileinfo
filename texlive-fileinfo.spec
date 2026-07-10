%global tl_name fileinfo
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.81a
Release:	%{tl_revision}.1
Summary:	Enhanced display of LaTeX File Information
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fileinfo
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fileinfo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fileinfo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fileinfo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides two packages, readprov and myfilist. The readprov
package provides a means of reading file information without loading the
body of the file. The myfilist package uses readprov and controls what
\listfiles will report.

