#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	XML
Summary:	Test::XML - Compare XML in perl tests
Summary(pl.UTF-8):	Test::XML - porówywanie XML-a w testach Perlowych
Name:		perl-Test-XML
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	490b487e07908358eb64a3c3c5b48143
URL:		https://metacpan.org/release/Test-XML
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-XML-Parser >= 2.34
BuildRequires:	perl-XML-SemanticDiff >= 0.95
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains generic XML testing tools.

%description -l pl.UTF-8
Ten moduł zawiera ogólne narzędzia do testowania XML-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/XML.pm
%{perl_vendorlib}/Test/XML
%{_mandir}/man3/Test::XML.3pm*
%{_mandir}/man3/Test::XML::*.3pm*
