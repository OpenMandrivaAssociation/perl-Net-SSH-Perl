%define	upstream_name	 Net-SSH-Perl
%define upstream_version 1.37

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl client Interface to SSH

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Math::Pari)
BuildRequires:	perl(Math::GMP)
BuildRequires:	perl(String::CRC32)
BuildRequires:	perl(Convert::PEM)
BuildRequires:	perl(Crypt::IDEA)
BuildRequires:	perl(Crypt::DH)
BuildRequires:	perl(Crypt::DSA)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Digest::HMAC)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::BubbleBabble)
BuildRequires:	perl(Crypt::RSA)
BuildArch:	noarch

%description
Net::SSH::Perl is an all-Perl module implementing an SSH
(Secure Shell) client. It is compatible with both the SSH-1
and SSH-2 protocols.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
# test hang... :\
# make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Net
%{_mandir}/man*/*



