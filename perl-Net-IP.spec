#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IP
Summary:	Net::IP - Perl extension for manipulating IPv4/IPv6 addresses
Summary(pl):	Net::IP - rozszerzenie Perla s³u¿±ce do manipulacji adresami IPv4/IPv6
Name:		perl-Net-IP
Version:	1.20
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	73c5941562833d5ca7ca7c3bff7983fe
Patch0:		%{name}-interpreter-path.patch
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Modu³ Perla Net::IP zawiera funkcje operuj±ce na adresach IPv4/IPv6.
Modu³u tego mo¿na u¿ywaæ jako klasy umo¿liwiaj±cej u¿ytkownikowi
tworzenie obiektów IP, którymi mog± byæ pojedyncze adresy, prefiksy,
czy te¿ zakresy adresów. Dostêp do wiêkszo¶ci funkcji mo¿liwy jest
równie¿ drog± proceduraln±. Wiêkszo¶æ procedur mo¿e w sposób
przezroczysty operowaæ zarówno na adresach IPv4, jak i IPv6.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
