AC_INIT([PellMon], [0.7.0])

AM_INIT_AUTOMAKE([foreign])
AM_PATH_PYTHON([2.7])

AC_PROG_MKDIR_P

AC_PROG_SED

AC_ARG_WITH([user_srv],
	AS_HELP_STRING([--with-user_srv=USER], [system user for pellmonsrv]),
	[],
	[with_user_srv=$(whoami)])

AC_SUBST([user_srv], [$with_user_srv])

AC_ARG_WITH([user_web],
	AS_HELP_STRING([--with-user_web=USER], [system user for pellmonweb]),
	[],
	[with_user_web=$(whoami)])

AC_SUBST([user_web], [$with_user_web])


dnl This options sets paths to point to source directory
AC_ARG_ENABLE([debug],
[  --enable-debug    Turn on debugging],
[case "${enableval}" in
  yes) debug=true ;;
  no)  debug=false ;;
  *) AC_MSG_ERROR([bad value ${enableval} for --enable-debug]) ;;
esac],[debug=false])
AM_CONDITIONAL([DEBUG], [test x$debug = xtrue])

AC_CONFIG_FILES([ \
Makefile \
initscript/Makefile \
data/Makefile \
src/Makefile \
src/conf.d/Makefile \
src/Pellmonsrv/Makefile \
src/Pellmonsrv/yapsy/Makefile \
src/Pellmonsrv/plugins/Makefile \
src/Pellmonsrv/plugins/testplugin/Makefile \
src/Pellmonsrv/plugins/scottecom/Makefile \
src/Pellmonsrv/plugins/raspberrygpio/Makefile \
src/Pellmonsrv/plugins/customalarms/Makefile \
src/Pellmonsrv/plugins/calculate/Makefile \
src/Pellmonsrv/plugins/owfs/Makefile \
src/Pellmonsrv/plugins/silolevel/Makefile \
src/Pellmonsrv/plugins/pelletcalc/Makefile \
src/Pellmonsrv/plugins/consumption/Makefile \
src/Pellmonsrv/plugins/cleaning/Makefile \
src/Pellmonsrv/plugins/onewire/Makefile \
src/Pellmonsrv/plugins/heatingcircuit/Makefile \
src/Pellmonsrv/plugins/nbecom/Makefile \
src/Pellmonsrv/plugins/openweathermap/Makefile \
src/Pellmonsrv/plugins/exec/Makefile \
src/Scotteprotocol/Makefile \
src/Pellmonweb/Makefile ])

AC_OUTPUT
