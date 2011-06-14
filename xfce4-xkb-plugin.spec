%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A plugin for the Xfce4 panel displaying keyboard layout
Name:		xfce4-xkb-plugin
Version:	0.5.4.1
Release:	%mkrel 1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-xkb-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	intltool
BuildRequires:	libxklavier-devel >= 5.0
BuildRequires:	librsvg2-devel
BuildRequires:	libwnck-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	libxfce4ui-devel
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-xkb-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A plugin for the Xfce4 panel displaying keyboard layout.
The plugin may be used as an indicator for the current layout
and to switch layouts.
The layouts must be defined either in XF86Config or by 
xetskbmap tool.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unneeded devel files
rm -f %{buildroot}/%{_libdir}/xfce4/panel-plugins/*.a

%find_lang %{name}

%clean
rm -rf  %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%dir %{_datadir}/xfce4/xkb
%{_datadir}/xfce4/xkb/*
%{_datadir}/xfce4/panel-plugins/xkb-plugin.desktop
%{_libdir}/xfce4/panel-plugins/
