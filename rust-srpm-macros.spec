Summary:        RPM macros for building Rust source packages
Name:		rust-srpm-macros
Version:	23
Release:	1
Group:		System/Packaging
License:	MIT
URL:		https://pagure.io/fedora-rust/rust2rpm
Source:		https://pagure.io/fedora-rust/rust2rpm/archive/v%{version}/rust2rpm-v%{version}.tar.gz
BuildArch:	noarch

%description
RPM macros for building Rust source packages.

%prep
%autosetup -n rust2rpm-v%{version} -p1
# https://pagure.io/koji/issue/659
sed -i -e 's/i686/%%{ix86}/' data/macros.rust-srpm
sed -i -e 's/x86_64/%%{x86_64}/' data/macros.rust-srpm
sed -i -e 's/armv7hl/armv7hnl/' data/macros.rust-srpm

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} data/macros.rust-srpm

%files
%license LICENSE
%{_rpmmacrodir}/macros.rust-srpm
