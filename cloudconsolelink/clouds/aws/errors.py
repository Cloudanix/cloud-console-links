class AWSLinkerError(ValueError):
    """Base class for AWS linker errors."""


class ARNTooShortError(AWSLinkerError):
    """Raised when an ARN is missing required segments."""


class InvalidARNError(AWSLinkerError):
    """Raised when an ARN is malformed."""


class InvalidPartitionError(AWSLinkerError):
    """Raised when an ARN contains an unsupported partition."""


class InvalidServiceError(AWSLinkerError):
    """Raised when an ARN contains an unknown AWS service."""


class UnsupportedResourceError(AWSLinkerError):
    """Raised when a known AWS service resource has no direct link mapping."""
