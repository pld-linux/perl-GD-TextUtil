# TODO
# - fonts-TTF-Dustismo_Sans package:
#   /usr/share/fonts/TTF/Dustismo_Sans.ttf

# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	GD
%define		pnam	TextUtil
Summary:	GD::Text - text utilities for use with GD
Summary(pl.UTF-8):	GD::Text - narzędzia do obróbki tekstu do użycia z GD
Name:		perl-GD-TextUtil
Version:	0.86
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/GD/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	941ad06eadc86b47f3a32da405665c41
Patch0:		%{name}-defaultttfdir.patch
URL:		http://search.cpan.org/dist/GDTextUtil/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 4.1-13
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a font-independent way of dealing with text in
GD, for use with the GD::Text::* modules and GD::Graph.

%description -l pl.UTF-8
Moduł ten udostępnia niezależne od fontu narzędzia do obróbki tekstu
w GD. Do użytku z modułami GD::Text::* i GD::Graph.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_fontsdir}/TTF}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p *.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/GD/Text.pm
%{perl_vendorlib}/GD/Text
%{_mandir}/man3/GD::Text*.3pm*
%{_examplesdir}/%{name}-%{version}
%{_fontsdir}/TTF/Dustismo_Sans.ttf
