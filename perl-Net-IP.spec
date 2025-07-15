#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Net
%define		pnam	IP
Summary:	Net::IP - Perl extension for manipulating IPv4/IPv6 addresses
Summary(pl.UTF-8):	Net::IP - rozszerzenie Perla służące do manipulacji adresami IPv4/IPv6
Name:		perl-Net-IP
Version:	1.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3a98e3ac45d69ea38a63a7e678bd716d
Patch0:		%{name}-interpreter-path.patch
URL:		http://search.cpan.org/dist/Net-IP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::IP Perl module provides functions to deal with IPv4/IPv6
addresses. The module can be used as a class, allowing the user to
instantiate IP objects, which can be single IP addresses, prefixes, or
ranges of addresses. There is also a procedural way of accessing most
of the functions. Most subroutines can take either IPv4 or IPv6
addresses transparently.

%description -l pl.UTF-8
Moduł Perla Net::IP zawiera funkcje operujące na adresach IPv4/IPv6.
Modułu tego można używać jako klasy umożliwiającej użytkownikowi
tworzenie obiektów IP, którymi mogą być pojedyncze adresy, prefiksy,
czy też zakresy adresów. Dostęp do większości funkcji możliwy jest
również drogą proceduralną. Większość procedur może w sposób
przezroczysty operować zarówno na adresach IPv4, jak i IPv6.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install ipcount $RPM_BUILD_ROOT%{_bindir}
install iptab $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/IP.pm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man3/*
