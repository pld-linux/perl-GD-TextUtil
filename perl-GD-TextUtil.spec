#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	TextUtil
Summary:	GD::Text - text utilities for use with GD
Summary(pl):	GD::Text - narzêdzia do obróbki tekstu do u¿ycia z GD
Name:		perl-GD-TextUtil
Version:	0.86
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	941ad06eadc86b47f3a32da405665c41
Patch0:		%{name}-defaultttfdir.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 4.1-13
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a font-independent way of dealing with text in
GD, for use with the GD::Text::* modules and GD::Graph.

%description -l pl
Modu³ ten udostêpnia niezale¿ne od fontu narzêdzia do obróbki tekstu
w GD. Do u¿ytku z modu³ami GD::Text::* i GD::Graph.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}
%patch0 -p1

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

install demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install *.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

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
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
%{_fontsdir}/TTF/*
